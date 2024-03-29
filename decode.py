from myFunction import set1,set0,get_bit,get_xor,txt_to_bin,bin_to_txt,get_pos_array
import cv2

pos_array = get_pos_array("password")
pa_ln = len(pos_array)


txt_bit = ""
txt_ln = 88  # this is the input text length, you should put this manualy. because, there have no end-point-condition



image = cv2.imread("output.png")
h,w,ch = image.shape



msb_p = 8
txt_b_cntr = 0
pss_a_cntr = 0
flag = True



for x in range(0,w):
    for y in range(0,h):
        pix_num = image[y,x][0]
        if get_bit(pix_num,msb_p) == 1:     #------- filtering
            

            p = pos_array[pss_a_cntr]       #------- get position from pos_array
            pss_a_cntr += 1
            if pss_a_cntr == pa_ln:
                pss_a_cntr = 0


            im_b = get_bit(pix_num,p+1)     #------- get pixel position bit

            im_b0 = get_bit(pix_num,1)      #------- get pixel LSB


            xor_b = get_xor(im_b,im_b0)

            if xor_b == True:               #------- retrive text bit
                txt_bit += '1'
            else:
                txt_bit += '0'




            txt_b_cntr += 1
            if txt_b_cntr >= txt_ln:
                flag = False
                break

    if flag == False:
        break

            
txt = bin_to_txt(txt_bit)

print(txt)
