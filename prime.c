
/*#include<stdio.h>
int main()
{
    int i=1,count=0,n;
    printf("Enter the number:");
    scanf("%d",&n);
    while(i<=n)
    {
        if(n%i==0)
        {
            count=count+1;
        }
        i++;
    }
    if(count==2)
        printf("%d is prime number\n",n);  
    else
        printf("%d is not a prime number\n",n);
    return 0;
}*/

#include<stdio.h>
int main()
{
    int i,count=0,n;
    printf("Enter the number:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        if(n%i==0)
        {
            count=count+1;
        }
    }
    if(count==2)
        printf("%d is prime number\n",n);  
    else
        printf("%d is not a prime number\n",n);
    return 0;
}

/*#include<stdio.h>
int main()
{
    int i=1,count=0,n;
    printf("Enter the number:");
    scanf("%d",&n);
    do
    {
        if(n%i==0)
        {
            count=count+1;
        }
        i++;
    }while(i<=n);
    if(count==2)
        printf("%d is prime number\n",n);  
    else
        printf("%d is not a prime number\n",n);
    return 0;
}*/
