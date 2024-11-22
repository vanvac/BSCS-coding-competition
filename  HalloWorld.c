#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
//#include <math.h>
char *snakeToCamel(char *snakeStr) {
  int i = 0;
  int j = 0;
  int len = strlen(snakeStr);
  bool isNextUpper = false;
  char *camelStr = malloc(len + 1);

  for (i = 0; i < len; i++) {
    if (snakeStr[i] == '_'){
      isNextUpper = true;
      continue;
    }
    else if (isNextUpper) {
      // 32 is the distance bettween upper and lowercase characters in ASCII character set eg. d= 100 and D = 68 which is 32 less
      camelStr[j++] = toupper(snakeStr[i]);
      isNextUpper = false;
    }
    else {
      camelStr[j++] = snakeStr[i];
    }
  }
  camelStr[j] = '\0';
  return camelStr;
}

int main() {
  char *result = snakeToCamel("hallo_world");
  printf("%s", result);
  return 0;
}