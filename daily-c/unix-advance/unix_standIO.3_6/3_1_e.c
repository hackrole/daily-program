#include <fcntl.h>
#include <unistd.h>

/*
 * lseek用于为文件设置偏移量,
 * lseek(int filedes, off_t offset, int whence)
 * filedes为文件描述符, off_t为偏移量,
 * whence取(SEEK_SET:文件开始,SEEK_CUR:当前偏移量,SEEK_END:文件结尾)
 * lseek(filedes, 0, SEEK_CUR)可用与判断文件是否可以设置便宜量
 */
int main(void){
  if(lseek(STDIN_FILENO, 0, SEEK_CUR) == -1){
	printf("canot seek\n");
  }else{
	printf("seek ok\n");
  }
  exit(0);
}
