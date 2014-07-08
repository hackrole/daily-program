#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>


int main(void){
  char buff[256];
  int error;
  lua_State *L = lua_open(); // open lua
  luaopen_base(L); // open lua basic lib
  luaopen_table(L); // open lua table lib
  luaopen_io(L); // open I/O lib
  luaopen_string(L); // open string lib
  luaopen_math(L); // open math lib

  while(fgets(buff, sizeof(buff), stdin) != NULL){
    error = luaL_loadbuffer(L, buff, strlen(buff),
        "line") || lua_pcal(L, 0, 0, 0);
    if(error){
      fprintf(stderr, "%s", lua_tostring(L, -1));
      lua_pop(L, 1); // pop error message from lua stack
    }
  }
  lua_close(L);
  return 0;
}
