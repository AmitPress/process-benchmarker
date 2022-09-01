#include<iostream>
#include<stdlib.h>
using namespace std;

long long fib(int n){
    if(n < 2) return 1;
    return fib(n-1)+fib(n-2);
}

int main(int argc, char *argv[]){
    cout<<fib(atoi(argv[1]));
}