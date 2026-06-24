import numpy as np

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.n_states = size * size
        self.terminal_states = {0, self.n_states - 1}
        self.actions = [0, 1, 2, 3]          # U, R, D, L
        self.action_names = ['U', 'R', 'D', 'L']
    
    def is_terminal(self, s):
        return s in self.terminal_states
    
    def get_next_state(self, s, a):
        if self.is_terminal(s):
            return s
        row, col = divmod(s, self.size)
        if a == 0: row = max(0, row-1)
        elif a == 1: col = min(self.size-1, col+1)
        elif a == 2: row = min(self.size-1, row+1)
        elif a == 3: col = max(0, col-1)
        return row * self.size + col
    
    def step(self, s, a):
        if self.is_terminal(s):
            return s, 0, True
        next_s = self.get_next_state(s, a)
        reward = -1
        done = self.is_terminal(next_s)
        return next_s, reward, done


def policy_evaluation(env, policy, gamma=0.9, theta=1e-4):
    V = np.zeros(env.n_states)
    iteration = 0
    while True:
        delta = 0
        V_new = np.copy(V)
        for s in range(env.n_states):
            if env.is_terminal(s):
                V_new[s] = 0
                continue
            v = 0.0
            for a_idx, a in enumerate(env.actions):
                pi_prob = policy[s, a_idx]
                if pi_prob == 0: continue
                next_s, r, _ = env.step(s, a)
                v += pi_prob * (r + gamma * V[next_s])
            V_new[s] = v
            delta = max(delta, abs(V_new[s] - V[s]))
        V = V_new
        iteration += 1
        if delta < theta:
            break
    return V, iteration


# Usage
env = GridWorld(size=4)
random_policy = np.ones((env.n_states, 4)) / 4
random_policy[list(env.terminal_states)] = 0

V, iters = policy_evaluation(env, random_policy, gamma=0.9, theta=1e-4)
print(f"Converged in {iters} iterations")
print("Value grid:\n", V.reshape(4,4).round(2))