#include<iostream>
#include<algorithm>
using namespace std;

struct Item 
{
    int Weight ;
    int Value ;
    double ratio ;
    
};

bool compare(Item a , Item b)
{
    return a.ratio>b.ratio ;
}

double fractionalknapsack(Item items[],int n,int capacity)
{
    sort(items,items+n,compare) ;
    
    double totalValue = 0.0 ;
    int CurrentWeight = 0 ;
    
    for(int i = 0 ; i < n ; i++)
    {
        if(CurrentWeight+items[i].Weight <= capacity)
        {
            CurrentWeight += items[i].Weight ;
            totalValue += items[i].Value ;
            cout<<"Adding item with Weight"<<items[i].Weight<<"and value"<<
            "(Full item) \n ";
        }
        else
        {
            int remainingWeight = capacity - CurrentWeight ;
            double Fraction = (double) CurrentWeight/items[i].weight ;
            totalValue += Fraction * items[i].value ;
            CurrentWeight += remainingWeight ;
            cout<<"Adding"<<Fraction<<"item with weight"<<items[i].Weight<<
            "and value"<<items[i].Value<<"\n";
            break;
        }
    }
    return totalValue;
}

int main()
{
    int n , capacity ;
    
    cout<<"Enter the number of items :- \n " ;
    cin>>n
    
    cout<<"Enter the capacity of kanpsack :- \n " ;
    cin>>capacity;
    
    Item items[n];
    for(int i = 0 ; i < n ; i++ )
    {
        cout<<"Enter the weight and value of items " << i + 1 << " :- \n ";
        cin>>items[i].Weight>>items[i].Value ;
        double ratio = (double) items[i].Value/items[i].Weight;
    }
    
    double maxValue = fractionalknapsack(items , n , capacity);
    cout<<"Maximum Value of Knapsack is "<<maxValue<<endl;
    
    return 0 ;
}
