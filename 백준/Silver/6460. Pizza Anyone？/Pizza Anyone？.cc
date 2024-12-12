#include <stdio.h>
#include <string.h>
#define MAX_PEOPLE 16
#define MAX_TOPPINGS 16

int main()
{
    unsigned long int wants[MAX_PEOPLE];
    unsigned long int hates[MAX_PEOPLE];
    int personId;
    unsigned long int pizzaId;

    char input[1024];

    while (1) {
        personId = 0;
        while (1) {
            if (fgets(input, sizeof(input), stdin) == NULL) {
                // 입력이 끝나면 프로그램 종료
                return 0;
            }
            if (input[0] == '.' && strlen(input) == 2) {
                break;
            }

            wants[personId] = 0;
            hates[personId] = 0;

            for (int i = 0; input[i] != '\0' && input[i] != '\n'; ++i) {
                if (input[i] == '+') {
                    wants[personId] |= (1LU << (input[++i] - 'A'));
                }
                else if (input[i] == '-') {
                    hates[personId] |= (1LU << (input[++i] - 'A'));
                }
            }

            ++personId;
        }

        int nPersons = personId;
        pizzaId = 0;
        int found = 0; // 피자 조합이 유효한지 확인하는 플래그
        do {
            for (personId = 0; personId < nPersons; ++personId) {
                if ((pizzaId & wants[personId]) || (~pizzaId & hates[personId])) {
                    // 조건 만족
                }
                else {
                    break;
                }
            }

            if (personId == nPersons) {
                found = 1; // 모든 사람이 만족
                break;
            }

            ++pizzaId;
        } while (pizzaId != (1LU << MAX_TOPPINGS));

        if (found) {
            int toppingId;
            printf("Toppings: ");
            for (toppingId = 0; toppingId < MAX_TOPPINGS; ++toppingId)
                if ((pizzaId >> toppingId) & 1)
                    printf("%c", toppingId + 'A');
            printf("\n");
        }
        else {
            printf("No pizza can satisfy these requests.\n");
        }
    }

    return 0;
}
