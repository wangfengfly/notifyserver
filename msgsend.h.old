#ifndef _HXMT_NET_H_
#define _HXMT_NET_H_

#ifdef WIN32
#ifdef SEND_EXPORTS
#define SENDEXPORT _declspec(dllexport)
#else
#define SENDEXPORT _declspec(dllimport)
#endif
#else
#if __GNUC__ >= 4
#define SENDEXPORT __attribute__ ((visibility("default")))
#else
#define SENDEXPORT extern "C" 
#endif
#endif

namespace hxmt {
namespace msg {

typedef void (RecieveFunc)(const char* missionID,const char* msg);

void SENDEXPORT SetConnect(const char* ip,const char* port);
void SENDEXPORT SetRecieve(int port,RecieveFunc* callback);
int SENDEXPORT MsgSend(const char* missionID,const char* msg);
void SENDEXPORT Release();
}//End namespace msg
}//End namespace dpgs

#endif
