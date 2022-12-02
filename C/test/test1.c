#include<stdio.h>
#include<stdlib.h>

int prt_esc_char(const char *s)
{
    int n = 0;
    while (*s != '\0') {
        if (*s >= 20) {
            putchar(*s);
            n++;
        } else {
            switch (*s) {
                case '\n':
                    putchar('\\');
                    putchar('n');
                    n += 2;
                    break;
                case '\r':
                    putchar('\\');
                    putchar('r');
                    n += 2;
                    break;
                case '\t':
                    putchar('\\');
                    putchar('t');
                    n += 2;
                    break;
                case '\b':
                    putchar('\\');
                    putchar('b');
                    n += 2;
                    break;
                default:
                    putchar('\\');
                    fprintf(stdout, "%02X", *s);
                    n += 3;
                    break;
            }
        }
        s++;
    }
    return n;
}

int main()
{
    char line[20] = "hello  world\n";
    int len = prt_esc_char(line);
    printf("%d\n", len);
}