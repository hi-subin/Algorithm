import { TreeNode } from "../TreeNode";

function maxDepth(root: TreeNode | null): number {
    let height = 0;

    if (root !== null) {
        height = 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    return height;
};