#include<stdio.h>
#include<conio.h>
void table(int n)
{
	int i;

	for(i=1;i<=10;i++)
	{
		printf("%d*%d=%d\n",n,i,n*i); 
	}
	
}
int main()
{
	int n1,n2;
	printf("enter a number");
	scanf("%d",&n1);
	table(n1);
	printf("enter a number");
	scanf("%d",&n2);
	table(n2);
}
