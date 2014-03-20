#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

#define RWRWRW (S_IRUSR|S_IWUSR|S_IRGRP|S_IWGRP|S_IROTH|S_IWOTH)
#define RW (S_IRGRP|S_IWGRP|S_IROTH|S_IWOTH)

/*
 * umask函数为进程设置文件权限屏蔽字
 * umask屏蔽的权限,建立文件指定无效
 */
int main(int argc, char *argv[])
{
  umask(0);
  if(creat("foo", RWRWRW) < 0){
	printf ("create error for foo\n");
  }
  umask(RW);
  if(creat("bar", RWRWRW) < 0){
	printf ("create error for bar\n");
  }
  return 0;
}
