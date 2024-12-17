#include <stdio.h>

__int64 __fastcall calc(int a1)
{
    int i; // [rsp+8h] [rbp-1Ch]
    __int64 v3; // [rsp+Ch] [rbp-18h]
    __int64 v4; // [rsp+14h] [rbp-10h]
    __int64 v5; // [rsp+1Ch] [rbp-8h]

    if (!a1)
        return 0LL;
    if (a1 == 1)
        return 1LL;
    v3 = 0LL;
    v4 = 1LL;
    for (i = 2; i <= a1; ++i)
    {
        v5 = v3 + v4;
        v3 = v4;
        v4 = v5;
    }
    return v4;
}

void main()
{
    for (int i = 0; i <= 14; i++)
    {
        printf("%llu", calc(i));
    }
}