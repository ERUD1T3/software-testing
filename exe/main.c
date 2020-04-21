#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


#define TRUE 1
#define FALSE 0

int isOneToOne(int **arr, int d, int r)
{
  int i, j;
  int count = 0;
  for (i = 0; i < d; i++)
  {
    for (j = 0; j < r; j++)
    {
      if (arr[i][j] == 1)
      {
       	count++;
      }
    }
    if (count > 1 || count == 0)
    {
      return FALSE;
    }
    count = 0;
  }
  return TRUE;
}

int isOnto(int **arr, int d, int r)
{
  int i, j, k;
  int checkCol[r];

  for (k = 0; k < r; k++)
  {
    checkCol[k] = 0;
  }

  for(i = 0; i < d; i++)
  {
    for(j = 0; j < r; j++)
    {
      if (arr[i][j] == 1)
      {
        checkCol[j] = 1;
      }
    }
  }

  for (k = 0; k < r; k++)
  {
    if (checkCol[k] == 0)
    {
      return FALSE;
    }
  }
  return TRUE;
}

int isReflexive(int **arr, int d, int r)
{
  int i;
  if (d == r) {
    for (i = 0; i < d; i++)
    {
      if (arr[i][i] != 1)
      {
        return FALSE;
      }
    }
  }
  else
  {
    return FALSE;
  }
  return TRUE;
}

int isFunction(int **arr, int d, int r)
{
  int i, j;
  int count = 0;
  for (i = 0; i < d; i++)
  {
    for (j = 0; j < r; j++)
    {
      if (arr[i][j] == 1)
      {
        count++;
      }
    }
    if (count != 1)
    {
      return FALSE;
    }
    count = 0;
  }
  return TRUE;
}


int main(int argc, char *argv[])
{

  char* generator = argv[1];
  char* onetoone = "onetoone";
  char* onto = "onto";
  char* reflex = "reflex";
  char* func = "func";
  

  //Get length of function
  int x, y, num, count;
  scanf("%d", &num);

  int i, j, isReflex, isFunc, isOn, isOto;

  int domain[num], range[num], domainSize = 0, rangeSize = 0;

  for (i = 0; i < num; i++)
  {
    scanf("%d %d", &domain[i], &range[i]);
    if (domain[i] > 0 && domain[i] < num + 1 && range[i] > 0 && range[i] < num + 1)
    {
      if (domain[i] > domainSize)
      {
        domainSize = domain[i];
      }
      if (range[i] > rangeSize)
      {
        rangeSize = range[i];
      }
    }
  }

  //Setup dynamicArray
  int **dynamicArray;
  dynamicArray = calloc(domainSize, sizeof(int*));
  for (i = 0; i < domainSize; i++)
  {
    dynamicArray[i] = calloc(rangeSize, sizeof(int*));
  }

  for (i = 0; i < domainSize; i++)
  {
    dynamicArray[domain[i] - 1][range[i] - 1] = 1;
  }

  if (strcmp(generator, onetoone) == 0)
  {
    isOto = isOneToOne(dynamicArray, domainSize, rangeSize);
    if (isOto == 1)
    {
      printf("\nIs one to one\n");
    }
    else
    {
      printf("\nIs not one to one\n");
    }

  }
  else if (strcmp(generator, onto) == 0)
  {
    isOn = isOnto(dynamicArray, domainSize, rangeSize);
    if (isOn == 1)
    {
      printf("\nIs onto\n");
    }
    else
    {
      printf("\nIs not onto\n");
    }
  }
  else if (strcmp(generator, reflex) == 0)
  {
    isReflex = isReflexive(dynamicArray, domainSize, rangeSize);
    if (isReflex == 1)
    {
      printf("\nIs reflexive\n");
    }
    else
    {
      printf("\nIs not reflexive\n");
    }
  }
  else if (strcmp(generator, func) == 0)
  {
    isFunc = isFunction(dynamicArray, domainSize, rangeSize);
    if (isFunc == 1)
    {
      printf("\nIs function\n");
    }
    else
    {
      printf("\nIs not function\n");
    }
  } else {
    printf("Wrong Input\n");
  }

  return 0;
}
