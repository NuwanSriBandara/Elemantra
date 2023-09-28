import cv2
import numpy as np

def ImagePath(path):

    bounding_boxes = []
    confidences = []
    class_numbers = []

    image_input = cv2.imread(path)
    blob = cv2.dnn.blobFromImage(image_input, 1/255.0, (416,416), swapRB=True, crop=False)
    blob_to_show = blob[0,:,:,:].transpose(1,2,0)
    network.setInput(blob)
    output_from_network = network.forward(layers_names_output)
    h,w = image_input.shape[:2]

    for result in output_from_network:
        for detection in result:
            scores = detection[5:]
            class_current = np.argmax(scores)
            confidence_current = scores[class_current]
            if confidence_current > probability_minimum:
                box_current = detection[0:4] * np.array([w, h, w, h])
                x_center, y_center, box_width, box_height = box_current.astype('int')
                x_min = int(x_center-(box_width/2))
                y_min = int(y_center-(box_height/2))
                bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)

    # %matplotlib inline
    # plt.rcParams['figure.figsize'] = (5.0,5.0)
    # plt.imshow(cv2.cvtColor(image_input, cv2.COLOR_BGR2RGB))
    # plt.show()

    labels2=[]
    for item in sorted(set(class_numbers)):
        labels2+=[labels[item]]

    return labels2

