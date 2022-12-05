#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int SIZE = 80;

int pstr_scan(char* str, int size);
void pstr_print(const char* str, int length);


int pstr_scan(char *str, int size){
    int i=0;
    for(char c=1; c!=-1&&c!=32; i++){
        c=(char)getchar();
        str[i]=c;
    }
    for(int k=0; k<i; k++){
        printf("%d ", str[k]);
    }
    printf("\n%d", i);
    return i-1;
}

void pstr_print(const char *str, int length){
    for(int i=0; i<length; i++){
        printf("%c", str[i]);
    }
}


int main()
{
    char line[SIZE];

    int length = pstr_scan(line, SIZE);
    //pstr_print(line, length);
    
  return 0;
}