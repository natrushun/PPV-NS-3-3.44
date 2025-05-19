#ifndef PPV_GLOBALRATE_SINGLETON_H
#define PPV_GLOBALRATE_SINGLETON_H

#include "ns3/singleton.h"
#include "ns3/simulator.h"

#include <string>
# include <map>


namespace ns3 {
	
class PpvGlobalRateSingleton : public Singleton<PpvGlobalRateSingleton> {
public:
	void addRate(std::string op, std::string markerName, float R);
	float getRate(std::string op);
	float getMarkerRate(std::string marker);
	void setUpdateOperatorsRateSec(float updateSec);
	void setFlowTimeoutSec(float _flowtimeoutSec);


private:
	std::map<std::string, int> globalRates;
	std::map<std::string, int> globalRatesInfo;
	std::map<std::string, int> markerRates;
	std::map<std::string, int> markerRatesInfo;
	std::map<std::string, std::string> opOfmarker;
	float lastSendInfo = 0.0;
	std::map<std::string, float> lastTimeOfRate;
	float updateOperatorsRateSec = 0.0;	//sec
	float flowtimeoutSec = 0.5;
	
};

} // namespace ns3

#endif /* PPV_GLOBALRATE_SINGLETON_H */
