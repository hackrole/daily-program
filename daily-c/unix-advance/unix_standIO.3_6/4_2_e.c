#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

/*
 * access函数用于测试实际用户是否
 * 具有对某文件的相应的权限
 */
int main(int argc, char *argv[]){
  if(argc != 2){
	printf("usage: a.out <pathname>\n");
	exit(-1);
  }
  if(access(argv[1], R_OK) < 0){
	printf("access error for %s", argv[1]);
	return -1;
  }else{
	printf("read access OK\n");
  }
  if(open(argv[1], O_RDONLY) < 0){
	printf("open error for %s", argv[1]);
	return -1;
  }else{
	printf("open for reading ok\n");
  }
  return 0;
}
