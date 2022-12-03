#include<stdio.h>
#include<stdlib.h>

void printEsc(char c)
{
    putchar('\\');
    if(c == '\n') putchar('n');
    if(c == '\r') putchar('r');
    if(c == '\t') putchar('t');
    if(c == '\b') putchar('b');
}
void printHex(char c)
{
    putchar('\\');
    int first = c / 16;
    int second = c % 16;
    putchar(first + 48);
    if (second < 10) putchar(second + 48);
    else putchar(second + 55);
}

int prt_esc_char(const char *s)
{
    int n = 0;
    while (*s != '\0') {
        if (*s >= 32) {
            putchar(*s);
            n++;
        } else {
            if (*s=='\n' || *s=='\r' || *s=='\t' || *s=='\b') {
                printEsc(*s);
                n += 2;
            } else {
                printHex(*s);
                n += 3;
            }
        }
        s++;
    }
    return n;
}

int main()
{
    char line[20] = {'\1','\x1f','\0'};
    int len = prt_esc_char(line);
    printf("%d\n", len);
}