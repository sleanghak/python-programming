#include<stdio.h>
#include<malloc.h>
# define TRUE 1
# define FALSE 0
/* Tree structure */
typedef struct TREE
{
  int data;
  struct TREE *left;
  struct TREE *right;
}TREE;
/* Insert data into Tree */
  TREE *InsertTree(data,p)
  int data;
  TREE *p;
{
/* Is Tree NULL */
if(!p)
{
  p = (TREE*)malloc(sizeof(TREE));
  p -> data = data;
  p -> left = NULL;
  p -> right = NULL;
  return(p);
}
/* Is data less than the parent element */
  if(data < p -> data)
  p -> left = InsertTree(data, p -> left);
else
/* Is data greater than the parent element */
  if(data > p -> data)
  p -> right = InsertTree(data, p -> right);
  return(p);
}
/* Print Tree */
void PrintTree(tree, level)
TREE *tree;
int level;
{
int i;
if(tree){
  PrintTree(tree -> right, level + 1);
  printf("\n");
  for(i = 0; i < level;i++)
  printf("\t");
  printf("%d", tree -> data);
  PrintTree(tree -> left, level + 1);
}
}

TREE *Del(r, q)
TREE *r, *q;
{
TREE *dnode;
if( r -> right != NULL)
r -> right = Del(r -> right, q);
else
{
dnode = r;
q -> data = r -> data;
r = r -> left;
free(dnode);
}
return( r );
}
/* Deletes the key from the tree */
TREE *DeleteElement(p, data)
TREE *p;
int data;{
  TREE *q;
  /*
   (is not p)--> មានន័យថាប្រសិន "P" ហ្នឹងអត់មានតម្លៃទេ
   Ex ប្រើសិនបើយើងចង់ insert តម្លៃមក Delete ហើយ
   តម្លៃដែលយើងចង់ sert មក Delete វាអត់មានវានឹងចូលលក្ខខ័ណ្ឌមួយហ្នឹង
  */
if(!p)
{
printf("\nNon Existent Data\n");
return(p);
}
else
{
  /*
   (data<p)-->មានន័យថា ឧទាហរណ៍បើសិនជាយើងចង់deleteលេខ 
   ណាមួយនៅក្នុង Treeហ្នឹងចឹង លុះត្រាតែមានលេខក្នុង Treeហ្នឹងបានយើង
   insert លេខទៅទើមអាច Delete បាន
  */
  if(data < p -> data)
  p -> left = DeleteElement(p -> left, data);
  else
  if(data > p -> data)
  p -> right = DeleteElement(p -> right, data);
    else
{
  q = p;
  if(q -> right == NULL)
{
  p = q -> left;
  free(q);
}
/*
 វារកឃើញអ្វីមួយដែលមានចង់ delete
*/
else
  if(q -> left == NULL)
{
  p = q -> right;
  free(q);
}
      else
  q -> left = Del(q -> left, q);
}
}
      return(p);
}


void main( )
{
  int data; //depth;
  TREE *tree = NULL;
  printf("\nTree-Insert and Delete Operations:\n");
    while(1)
{
  printf("\nKey to Insert <0>?");
  scanf("%d", &data);
  printf("%d\n", data);
  if(data == 0)
    break;
  tree = InsertTree(data, tree);
  printf("\nTree Display:\n");
  PrintTree(tree, 1);

}
    while(1)
{
  printf("\nKey to Delete <0>?");
  scanf("%d", &data);
  printf("%d\n", data);
  if(data == 0)
    break;
  tree = DeleteElement(tree, data);
  printf("\nTree Display:\n");
  PrintTree(tree, 1);

}
}