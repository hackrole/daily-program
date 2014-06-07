#include "../lib/unp.h"

void Sig_chld(int signo) {
  pid_t pid;
  int stat;

  pid = wait(&stat);
  printf("child %d terminated\n", pid);
  return;
}

