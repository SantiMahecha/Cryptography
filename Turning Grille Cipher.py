{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Turning Grille Cipher",
      "provenance": [],
      "authorship_tag": "ABX9TyP2uruotBJT3r+CSMcmEnJJ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "0UWlPvDBr2zi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        },
        "outputId": "aa151b93-5d3e-425e-9d8a-5fb08f9933d0"
      },
      "source": [
        "#@Santiago Mahecha Pinzón\n",
        "#smahechap@unal.edu.co\n",
        "\n",
        "print(\"-------------------------------------------------------Turning Grille Cipher Algotihm----------------------------------------------------------\\n\")\n",
        "\n",
        "def create_matrix(rows,columns,initial):\n",
        "    return [[initial for i in range(rows)]for j in range(columns)]\n",
        "\n",
        "size = int(input(\"Input the size of the grille: \"))\n",
        "print(\"\\n\")\n",
        "\n",
        "main_matrix = create_matrix(size,size,0) #Create main matrix\n",
        "\n",
        "print(\"Define the holes positions, 1 if there is a hole and 0 if there is not:\\n\")\n",
        "for i in range(0,size):\n",
        "    for j in range(0,size):\n",
        "        h = bool(int(input(f\"Input the {i} element of the {j} row of the key (KEY): \")))\n",
        "        main_matrix[i][j] = h\n",
        "print(\"\\n\")\n",
        "print(main_matrix)\n",
        "\n",
        "def locindex(c): #Get location of each character.\n",
        "    loc=list()\n",
        "    for i ,j in enumerate(main_matrix):\n",
        "        #print(i,j)\n",
        "        for m,n in enumerate(j):\n",
        "            #print(m,n)\n",
        "            if c == n:\n",
        "                loc.append(i)\n",
        "                loc.append(m)\n",
        "                return loc\n",
        "\n",
        "\n",
        "e = 1    \n",
        "while(e == 1):\n",
        "    print(\"\\n Choose an action to realize: \\n\")\n",
        "    choice=int(input(\"\\n 1.Encrytion \\n 2.Decryption \\n 3.Exit\\n\\n\"))\n",
        "    print(\"\\n\")\n",
        "\n",
        "    if choice==1:\n",
        "        encrypt()\n",
        "    elif choice==2:\n",
        "        decrypt()\n",
        "    elif choice==3:\n",
        "        e = 0\n",
        "    else:\n",
        "        print(\"Choose a correct option\\n\")  \n"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "-------------------------------------------------------Turning Grille Cipher Algotihm----------------------------------------------------------\n",
            "\n",
            "Input the size of the grille: 2\n",
            "\n",
            "\n",
            "Define the holes positions, 1 if there is a hole and 0 if there is not:\n",
            "\n",
            "Input the 0 element of the 0 row of the key (KEY): 0\n",
            "Input the 0 element of the 1 row of the key (KEY): 1\n",
            "Input the 1 element of the 0 row of the key (KEY): 1\n",
            "Input the 1 element of the 1 row of the key (KEY): 0\n",
            "\n",
            "\n",
            "[[False, True], [True, False]]\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}