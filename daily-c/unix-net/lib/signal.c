#include "unp.h"

Sigfunc *signal(int signo, Sigfunc *func) {
  struct sigaction act, oact;

  act.sa_handler = func;
  sigemptyset(&act.sa_mask);
  act.sa_flags = 0;

  if (signo == SIGALRM) {
#ifdef SA_INTERRUPT
    act.sa_flags |= SA_INTERRUPT; // sunos 4.x
#endif
  } else {
#ifdef SA_RESTART
    act.sa_flags |= SA_RESTART; // svr4, 44BSD
#endif
  }

  if(sigaction(signo, &act, &oact) < 0)
    return (SIG_ERR);
  return (oact.sa_handler);
}

