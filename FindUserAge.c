#include <stdio.h>
#include <math.h>
#include <time.h>


int main() {
  time_t result = time(NULL);
  printf("%s", ctime(&result));
  return 0;
}