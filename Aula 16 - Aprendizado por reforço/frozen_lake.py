'''
1. Alfa (α) - Taxa de Aprendizado:
Controla a velocidade com que o agente aprende novos valores de Q.
Função: Define o quanto o agente deve ajustar o valor aprendido com base em novas experiências.
Valor típico: Entre 0 e 1.
Próximo de 1: O agente atualiza rapidamente os valores Q (aprendizado rápido).
Próximo de 0: O agente atualiza muito lentamente (aprendizado lento).

2. Epsilon (ε) - Fator de Exploração:
O que é: Determina a probabilidade de o agente explorar (fazer uma ação aleatória) em vez de seguir a melhor ação aprendida.
Função: Equilibra a exploração (tentar ações novas) e a exploração (usar o que já sabe).
Valor típico: Entre 0 e 1.
Próximo de 1: O agente explora mais (toma muitas ações aleatórias).
Próximo de 0: O agente explora menos (segue a política aprendida).

3. Gama (γ) - Fator de Desconto:
O que é: Define a importância das recompensas futuras em comparação às recompensas imediatas.
Função: Controla quanto o agente se preocupa com o longo prazo.
Valor típico: Entre 0 e 1.
Próximo de 1: O agente valoriza mais as recompensas futuras (planejamento a longo prazo).
Próximo de 0: O agente foca mais nas recompensas imediatas (miopia).

Embora epsilon (ε) não apareça diretamente na equação, ele é fundamental para a escolha da ação
durante o processo de aprendizado. O agente usa a estratégia ε-greedy para escolher entre explorar
 (escolher uma ação aleatória) ou explorar (escolher a melhor ação aprendida até agora).

Com probabilidade ε, o agente escolhe uma ação aleatória (exploração).
Com probabilidade 1 - ε, o agente escolhe a ação com o maior valor Q no estado atual (exploração).

Como epsilon (ε) afeta o aprendizado:
Quando o agente escolhe uma ação aleatória (exploração), ele pode descobrir novos caminhos que
 levam a melhores recompensas, ajudando a construir uma Q-table melhor ao longo do tempo.
Quando o agente escolhe a ação com o maior valor Q (exploração), ele utiliza o conhecimento que
já adquiriu para maximizar a recompensa com base nas experiências anteriores.
Portanto, epsilon afeta qual ação é escolhida antes de aplicar a equação de Q-learning para
atualizar os valores de Q(s, a). A estratégia ε-greedy ajusta o balanço entre exploração e
exploração, o que influencia indiretamente o aprendizado e a atualização da Q-table.

Esses três parâmetros controlam como o agente aprende e toma decisões no Q-learning.

'''

import gym
import numpy as np
import matplotlib.pyplot as plt
import pickle

def run(episodes, is_training=True, render=False):

    env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=True, render_mode='human' if render else None)

    if(is_training):
        q = np.zeros((env.observation_space.n, env.action_space.n)) # init a 64 x 4 array
    else:
        f = open('frozen_lake8x8.pkl', 'rb')
        q = pickle.load(f)
        f.close()

    learning_rate_a = 0.9  # alpha or learning rate
    discount_factor_g = 0.0009  # gamma or discount rate. Near 0: more weight/reward placed on immediate state. Near 1: more on future state.
    epsilon = 1  # 1 = 100% random actions
    epsilon_decay_rate = 0.0001  # epsilon decay rate. 1/0.0001 = 10,000
    rng = np.random.default_rng()  # random number generator

    rewards_per_episode = np.zeros(episodes)

    for i in range(episodes):
        state = env.reset()[0]  # states: 0 to 63, 0=top left corner, 63=bottom right corner
        terminated = False  # True when fall in hole or reached goal
        truncated = False  # True when actions > 200

        while(not terminated and not truncated):
            if is_training and rng.random() < epsilon:
                action = env.action_space.sample()  # actions: 0=left, 1=down, 2=right, 3=up
            else:
                action = np.argmax(q[state, :])

            new_state, reward, terminated, truncated, _ = env.step(action)

            if is_training:
                q[state, action] = q[state, action] + learning_rate_a * (
                    reward + discount_factor_g * np.max(q[new_state, :]) - q[state, action]
                )

            state = new_state

        epsilon = max(epsilon - epsilon_decay_rate, 0)

        if epsilon == 0:
            learning_rate_a = 0.0001

        if reward == 1:
            rewards_per_episode[i] = 1

        # Impressão dos dados de cada episódio
        print(f"Episódio {i+1}/{episodes}: Recompensa = {reward}, Epsilon = {epsilon:.5f}")

    env.close()

    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        sum_rewards[t] = np.sum(rewards_per_episode[max(0, t-100):(t+1)])
    plt.plot(sum_rewards)
    plt.savefig('frozen_lake8x8.png')

    if is_training:
        f = open("frozen_lake8x8.pkl", "wb")
        pickle.dump(q, f)
        f.close()


if __name__ == '__main__':
    # run(15000)

    run(160, is_training=True, render=True)
