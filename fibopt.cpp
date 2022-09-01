#include<iostream>
#include<map>
#include<stdlib.h>
using namespace std;

long long fib(int n, map<int,int>& mp){
    if(mp.count(n)){
        return mp[n];
    }
    if(n <= 2){
        mp[1] = 1;
        mp[2] = 1;
        return mp[n];
    }
    mp[n] = fib(n-1, mp)+fib(n-2, mp);
    return mp[n];
}

// int main(){
//     map<int,int> mp;
//     int n;
//     cin>>n;
//     cout<<fib(n, mp);
// }
int main(int argc, char *argv[]){
    map<int,int> mp;
    cout<<fib(atoi(argv[1]), mp);
}