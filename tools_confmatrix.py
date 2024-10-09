from sklearn import metrics 

def show_confusion_matrix_extended (y_true, y_pred, labels = ["N", "P"], beta = 1.0):
    # --- counting
    cm = metrics.confusion_matrix(y_true, y_pred)
    TP = cm [1, 1]
    TN = cm [0, 0]
    FN = cm [1, 0]
    FP = cm [0, 1]

    # --- print confusion matrix
    lab_N = labels [0] [0:10]
    lab_P = labels [1] [0:10]
    print (f"  Confusion Matrix       |     predicted label     |")
    print (f"                         | {lab_N:<10s} | {lab_P:<10s} |")
    print (f"-------------------------+------------+------------+")
    print (f"              {lab_N:<10s} | TN={TN:7d} | FP={FP:7d} |")
    print (f"  true label  -----------+------------+------------+")
    print (f"              {lab_P:<10s} | FN={FN:7d} | TP={TP:7d} |")
    print (f"-------------------------+------------+------------+")

    # --- print additional metrices
    print ()
    P = TP + FN  # elements in positive class
    N = FP + TN  # elements in negative class

    accuracy = (TP + TN) / (P + N)  # metrics.accuracy_score (y_true, y_pred)
    print (f"    accuracy    = {accuracy:6.4f}")

    precision = TP / (TP + FP)      # metrics.precision_score (y_true, y_pred)
    print (f"    precision   = {precision:6.4f}")

    recall = TP / P                 # metrics.recall_score (y_true, y_pred)
    print (f"    recall      = {recall:6.4f}")

    FP_rate = FP / N
    print (f"    FP-rate     = {FP_rate:6.4f}")

    TP_rate = TP / P
    print (f"    TP-rate     = {TP_rate:6.4f}")

    F1_score = 2 * TP / (2 * TP + FN + FP)  # metrics.F1_score (y_true, y_pred)
    print (f"    F1-score    = {F1_score:6.4f}")

    if (beta != 1.0):
        Fbeta_score = (1 + beta **2) * TP / ( (1 + beta **2) * TP + FP + beta **2 * FN)
                                            # metrics.F1_score (y_true, y_pred, beta)
        print (f"    Fbeta-score = {Fbeta_score:6.4f}")

# --- test
if __name__ == "__main__":
    y_true_test = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    y_pred_test = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    labels = ["not hab", "hab"]
    show_confusion_matrix_extended (y_true_test, y_pred_test, labels, beta = 2.0)