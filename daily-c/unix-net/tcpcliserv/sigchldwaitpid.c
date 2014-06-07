#include "../lib/unp.h"

// 使用waitpid 代替 wait不能设置非堵塞问题
// 循环调用解决信号不排队问题
void sig_chld(int signo){
  pid_t pid;
  int stat;

  while( (pid = waitpid(-1, &stat, WNOHANG)) > 0){
    printf("child %d terminaated\n", pid);
  }
}
