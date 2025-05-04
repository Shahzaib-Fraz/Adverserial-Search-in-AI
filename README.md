# Adverserial-Search-in-AI

# Minimax vs Alpha-Beta Pruning

## 🧠 Minimax Algorithm

### ✅ Pros
- Guarantees the best possible move assuming the opponent plays optimally.
- Simple to implement and understand.
- Forms the basis of many adversarial search algorithms.

### ❌ Cons
- Exponential time complexity: O(b^d), where `b` is branching factor and `d` is depth.
- Inefficient for deep game trees.
- Evaluates every possible node, even when unnecessary.

---

## ✂️ Alpha-Beta Pruning (Optimized Minimax)

### ✅ Pros
- Prunes branches that won’t affect the final decision, reducing the number of nodes evaluated.
- Much faster than plain Minimax in practice.
- Same result as Minimax but with improved performance.
- Can go deeper in the search tree within the same time constraints.

### ❌ Cons
- Still exponential in worst case (O(b^d)), but improved in best case.
- Efficiency heavily depends on move ordering (best when good moves are evaluated early).
- Slightly more complex to implement than basic Minimax.

---

## 💡 Summary

| Feature             | Minimax       | Alpha-Beta Pruning     |
|---------------------|---------------|-------------------------|
| Time Complexity     | O(b^d)        | O(b^(d/2)) in best case |
| Space Complexity    | O(b * d)      | O(b * d)                |
| Optimality          | Yes           | Yes                     |
| Efficiency          | Low           | High (with good pruning)|
| Complexity          | Simple        | Moderate                |
