#include "../lib/unp.h"


/*
 * 对于已链接套接字(调用connect).
 * 不能使用send,改用read/write. 只能与一个对端互操作
 */
void dg_cli(FILE *fp, int sockfd, const SA *pservaddr, socklen_t servlen){
  int n;
  char sendline[MAXLINE], recvline[MAXLINE + 1];

  Connect(sockfd, (SA *)pservaddr, servlen);

  while (Fgets(sendline, MAXLINE, fp) != NULL){
    Write(sockfd, sendline, strlen(sendline));

    n = Read(sockfd, recvline, MAXLINE);

    // null terminal
    recvline[n] = 0;
    Fputs(recvline, stdout);
  }
}

