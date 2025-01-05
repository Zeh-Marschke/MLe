from sklearn import metrics 

def get_confusion_matrix_values (y_true, y_pred, beta = 1.0):
    values = {}
    # --- counting
    cm = metrics.confusion_matrix(y_true, y_pred)
    TP = cm [1, 1]
    TN = cm [0, 0]
    FN = cm [1, 0]
    FP = cm [0, 1]

    values ['TP'] = TP
    values ['TN'] = TN
    values ['FN'] = FN
    values ['FP'] = FP

    P = TP + FN  # elements in positive class
    N = FP + TN  # elements in negative class

    values ['acc'] = (TP + TN) / (P + N)  # metrics.accuracy_score (y_true, y_pred)
    values ['pre'] = TP / (TP + FP)       # metrics.precision_score (y_true, y_pred)
    values ['rec'] = TP / P               # metrics.recall_score (y_true, y_pred)
    values ['FPR'] = FP_rate = FP / N
    values ['TPR'] = TP / P
    values ['F1']  = 2 * TP / (2 * TP + FN + FP)  # metrics.F1_score (y_true, y_pred)
    values ['Fbeta'] = (1 + beta **2) * TP / ( (1 + beta **2) * TP + FP + beta **2 * FN)
                                          # metrics.F1_score (y_true, y_pred, beta)
    return values

def show_confusion_matrix_line (y_true, y_pred, beta=1.0, with_time=False, elapsed_time=0.0, asLaTeX=False):
    d = get_confusion_matrix_values (y_true, y_pred, beta=beta)
    sep = ''
    if asLaTeX:
        sep = '&'

    print (f" {d['TP']:6d} {sep} {d['FN']:6d} {sep} {d['FP']:6d} {sep} {d['TN']:6d} {sep}", end= "")
    print (f" {d['acc']:6.4f} {sep} {d['pre']:6.4f} {sep} {d['rec']:6.4f} {sep}", end="")
    print (f" {d['FPR']:6.4f} {sep} {d['TPR']:6.4f} {sep} {d['F1']:6.4f}{sep}", end="")
    if with_time:
        print (f"  {elapsed_time:6.1f} s", end="")
    print ()

def show_confusion_matrix_extended (y_true, y_pred, labels = ["Neg", "Pos"], beta=1.0):
    d = get_confusion_matrix_values (y_true, y_pred, beta=beta)
    
    # --- print confusion matrix
    lab_N = labels [0] [0:10]
    lab_P = labels [1] [0:10]
    print (f"  Confusion Matrix       |     predicted label     |")
    print (f"                         | {lab_N:<10s} | {lab_P:<10s} |")
    print (f"-------------------------+------------+------------+")
    print (f"              {lab_N:<10s} | TN={d['TN']:7d} | FP={d['FP']:7d} |")
    print (f"  true label  -----------+------------+------------+")
    print (f"              {lab_P:<10s} | FN={d['FN']:7d} | TP={d['TP']:7d} |")
    print (f"-------------------------+------------+------------+")
    print ()
    print (f"    F1-score    = {d['F1']:6.4f}")
    print (f"    accuracy    = {d['acc']:6.4f}")
    print (f"    precision   = {d['pre']:6.4f}    purity")
    print (f"    recall      = {d['rec']:6.4f}    sensitivity / efficiency")
    print (f"    FP-rate     = {d['FPR']:6.4f}    alpha-error")
    print (f"    TP-rate     = {d['TPR']:6.4f}    1 - beta-error")
    if (beta != 1.0):
        print (f"    Fbeta-score = {d['Fbeta']:6.4f}")


def show_confusion_matrix_extended_old (y_true, y_pred, labels = ["Neg", "Pos"], beta = 1.0, short=False):
    # --- counting
    cm = metrics.confusion_matrix(y_true, y_pred)
    TP = cm [1, 1]
    TN = cm [0, 0]
    FN = cm [1, 0]
    FP = cm [0, 1]

    # --- print confusion matrix
    lab_N = labels [0] [0:10]
    lab_P = labels [1] [0:10]
    if short:
        print ("short")
    else:
        print (f"  Confusion Matrix       |     predicted label     |")
        print (f"                         | {lab_N:<10s} | {lab_P:<10s} |")
        print (f"-------------------------+------------+------------+")
        print (f"              {lab_N:<10s} | TN={TN:7d} | FP={FP:7d} |")
        print (f"  true label  -----------+------------+------------+")
        print (f"              {lab_P:<10s} | FN={FN:7d} | TP={TP:7d} |")
        print (f"-------------------------+------------+------------+")
        print ()

    # --- print additional metrices
    P = TP + FN  # elements in positive class
    N = FP + TN  # elements in negative class

    accuracy = (TP + TN) / (P + N)  # metrics.accuracy_score (y_true, y_pred)
    precision = TP / (TP + FP)      # metrics.precision_score (y_true, y_pred)
    recall = TP / P                 # metrics.recall_score (y_true, y_pred)
    FP_rate = FP / N
    TP_rate = TP / P
    F1_score = 2 * TP / (2 * TP + FN + FP)  # metrics.F1_score (y_true, y_pred)
    if short:
        print (short)
    else:
        print (f"    F1-score    = {F1_score:6.4f}")
        print (f"    accuracy    = {accuracy:6.4f}")
        print (f"    precision   = {precision:6.4f}")
        print (f"    recall      = {recall:6.4f}")
        print (f"    FP-rate     = {FP_rate:6.4f}")
        print (f"    TP-rate     = {TP_rate:6.4f}")

    if (beta != 1.0):
        Fbeta_score = (1 + beta **2) * TP / ( (1 + beta **2) * TP + FP + beta **2 * FN)
                                            # metrics.F1_score (y_true, y_pred, beta)
        if short:
            print ("short")
        else:
            print (f"    Fbeta-score = {Fbeta_score:6.4f}")

# --- test
if __name__ == "__main__":
    y_true_test = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    y_pred_test = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    labels = ["not hab", "hab"]
    show_confusion_matrix_extended_old (y_true_test, y_pred_test, labels, beta = 2.0)

    #dict_values = get_confusion_matrix_values (y_true_test, y_pred_test, beta = 2.0)
    #print (dict_values)
    show_confusion_matrix_extended (y_true_test, y_pred_test, labels, beta = 2.0)
    show_confusion_matrix_line (y_true_test, y_pred_test, beta = 2.0)