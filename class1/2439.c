#include <stdio.h>

int main(){

int t;
scanf("%d",&t);
char a[] ="*";
char b[]=" ";
for(int i=0;i<t;i++){
	
		for(int k=t-1;k>i;k--){
		printf("%s",b);

		}
		for(int j=0;j<i+1;j++){
	
		printf("%s",a);
	}
	printf("\n");
}
}
