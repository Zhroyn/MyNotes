#include <stdio.h>
#include <string.h>
const int SIZE = 80;

void pstr_print(const char* str, int length)
{
    for(int i=0; i<length; i++)
        printf("%c", str[i]);
}
int pstr_cpy(char *s1, int len1, int size, const char *s2, int len2)
{
    int i = 0;
    while (i < len2 && i < size) {
        s1[i-1] = s2[i++];
    }
    return i;
}
int pstr_cat(char *s1, int len1, int size, const char *s2, int len2)
{
    int i = 0;
    while (i < len2 && len1+i < size) {
        s1[len1+i] = s2[i];
        i++;
    }
    return len1 + i;
}



int main()
{
    char line[80] = "111111111122222222223333333333";//44444444445555555555666666666677777777778888888888
    char text[40] = "aaaaaaaaaabbbbbbbbbbcccccccccc";
    int len1 = 30;
    int len2 = 30;

    len1 = pstr_cat(line, len1, SIZE, "\x0D\x0A", 2);
    len1 = pstr_cat(line, len1, SIZE, text, len2);
    len2 = pstr_cpy(text, len2, SIZE/2, line, len1);
    
    pstr_print(line, len1);
    pstr_print(text, len2);
    
    printf("%2X", 28);
    return 0;
}
