#include <fcntl.h>
#include <unistd.h>

char buf1[] = "abcdefghijk";
char buf2[] = "ABCDEFGHIJK";
#define FILE_MODE O_RDWR

int err_sys(char *log){
  printf("%s", log);
  exit(-1);
}

int main(void){
  int fd;
  
  if((fd = creat("file.hole", FILE_MODE)) < 0){
	
	err_sys("create error");
  }
  
  if(write(fd, buf1, 10) != 10){
	err_sys("buf1 write error");
  }//offset=10 now
  
  if(lseek(fd, 16384, SEEK_SET) == -1){
	err_sys("lseek error");
  }//offset=16384 now
  
  if(write(fd, buf2, 10) != 10){
	err_sys("buf2 write error!");
  }
  return 0;
}
