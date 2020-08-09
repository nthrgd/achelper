#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mode import Mode

def calcul_total(dep, list_accounts):
    modes = Mode.modes
    total = dep
    for i in range(len(list_accounts)):
        date, mode, montant = list_accounts[i]
        if mode == "VIREMENT":
            total += float(montant)
        elif mode in modes:
            total -= float(montant)
        else:
            print(f"INFO: Le mode de paiement '{mode}' (ligne {i + 1})", \
                  "n'est pas reconnu donc cette ligne n'est pas prise en", \
                  "compte dans le calcul du total.")
    return total
