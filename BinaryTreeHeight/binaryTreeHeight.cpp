#include <iostream>

int height(Node * root) {

         if (root == NULL)
            return -1;

        // Recurse over left and right subtrees
        int leftDepth = height(root->left), rightDepth = height(root->right);

        if (leftDepth > rightDepth) { return (leftDepth + 1); }
        else { return (rightDepth + 1); }
    }
