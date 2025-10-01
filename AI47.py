def alpha_beta(node, depth, alpha, beta, maximizingPlayer, tree):
    
    if depth == 0 or node not in tree:
        return node  

    if maximizingPlayer:  
        value = float('-inf')
        for child in tree[node]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False, tree))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  
        return value
    else:  
        value = float('inf')
        for child in tree[node]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True, tree))
            beta = min(beta, value)
            if beta <= alpha:
                break  
        return value

tree = {
    'A': ['B', 'C'],
    'B': [5, 6],
    'C': [7, 4]
}

optimal_value = alpha_beta('A', depth=2, alpha=float('-inf'), beta=float('inf'),
                           maximizingPlayer=True, tree=tree)

print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

