#include <stdio.h>

int main(){

int t;
scanf("%d",&t);
char a[] ="*";

for(int i=1; i<=t; i++){
	for(int j=0;j<=i-1;j++){
		printf("%s",a);
	}
	printf("\n");
}
}
