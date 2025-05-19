#include "ppv-globalRate-singleton.h"

namespace ns3 {
//update rate when packet arive
void PpvGlobalRateSingleton::addRate(std::string op, std::string markerName, float R) {
	float tnow = Simulator::Now ().GetSeconds ();
	 if (markerRates.find(markerName) != markerRates.end()) {
		 // mikor jott az utolso, ha 500 alatt nem jott uj, akkor 0 a rata
		 globalRates[op] -= markerRates[markerName];
	 }
	 lastTimeOfRate[markerName] = tnow;
	 opOfmarker[markerName] = op;
	 markerRates[markerName] = R;
	 globalRates[op] += R;
}

void PpvGlobalRateSingleton::setUpdateOperatorsRateSec(float updateSec) {
	 updateOperatorsRateSec = updateSec;
}

void PpvGlobalRateSingleton::setFlowTimeoutSec(float _flowtimeoutSec) {
	 flowtimeoutSec = _flowtimeoutSec;
}

float PpvGlobalRateSingleton::getRate(std::string op) {
	float tnow = Simulator::Now ().GetSeconds ();

	//ha valaki 500ms ota nem kuldott erteket akkor kilepett
	for (std::map<std::string, float>::iterator it = lastTimeOfRate.begin(); it != lastTimeOfRate.end(); ++it) {
		if (tnow - lastTimeOfRate[it->first] > flowtimeoutSec) {
			addRate(opOfmarker[it->first],it->first,0);
		}
	}
	
	//csak 500ms utan adja az uj erteket
	if (tnow - lastSendInfo > updateOperatorsRateSec) {
	// if (tnow - lastSendInfo > 0.1) {
		lastSendInfo = tnow;
		for (std::map<std::string, int>::iterator it = globalRates.begin(); it != globalRates.end(); ++it) {
		// for (const auto& kv : globalRates) {
			globalRatesInfo[it->first] = globalRates[it->first];
		}
		for (std::map<std::string, int>::iterator it = markerRates.begin(); it != markerRates.end(); ++it) {
		// for (const auto& kv : globalRates) {
			markerRatesInfo[it->first] = markerRates[it->first];
		}
	}
	
	return globalRatesInfo[op];
}

float PpvGlobalRateSingleton::getMarkerRate(std::string marker) {
	return markerRatesInfo[marker];
}

}