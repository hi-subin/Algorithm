class TreeNode {
    public val: number;
    public left: TreeNode | null;
    public right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function maxDepth(root: TreeNode | null): number {
    let height = 0;

    if (root !== null) {
        height = 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    return height;
};