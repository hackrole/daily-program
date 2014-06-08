#include "../apue.h"

int glob = 6; // ext varibale in initialization data

int main(int argc, char **argv){
  int var; // automatic varibale on the stack
  pid_t pid;

  var = 88;
  printf("before vfork\n"); // we do not flush the stdio

  if ((pid == vfork()) < 0){
    err_sys("vfork error");
  } else if(pid == 0){
    glob++;
    var++;
    _exit(0); // child terminate
  }

  // parent continue here
  printf("pid=%d, ppid=%d, glob=%d, var=%d\n", getpid(), getppid(), glob, var);
  exit(0);
}

