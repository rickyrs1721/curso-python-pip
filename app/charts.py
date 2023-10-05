import matplotlib.pyplot as plt

def generate_bar_chart(country, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./img/{country}.png')
    plt.close()
    # plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    # plt.show()
    plt.savefig('pie.png')
    plt.close()

#generate_bar_char()

if __name__ == '__main__':

    labels = ['a', 'b', 'c']
    values = [100, 200, 60]

    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)

