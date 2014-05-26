#include "../apue.h"

int glob = 6; // the ext varibale in initialization data
char buf[] = "a write to stdout\n";

int main(int argc, char **argv){
  int var; // automatic variable on the stack
  pid_t pid;

  var = 88;
  if (write(STDOUT_FILENO, buf, sizeof(buf)-1) != (sizeof(buf)-1)){
    err_sys("write error");
  }
  printf("before fork\n"); // we do not flush the output

  if( (pid = fork()) < 0 ){
    err_sys("fork error");
  } else if (pid == 0){
    glob++; // modify variable in the child
    var++;
  } else {
    sleep(2); //parent, wait for the cliend end
  }

  printf("pid = %d, ppid=%d, glob=%d, var=%d\n", getpid(), getppid(), glob, var);
  exit(0);
}

