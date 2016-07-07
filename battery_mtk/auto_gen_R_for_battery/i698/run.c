//

struct soc_zcv_array
{
    int soc;
    int zcv;//1000
};

struct vbat_Q_array
{
    float vbat;//1
    float q;// remap to soc
};
struct rbat_zcv_array
{
    int rbat;
    int zcv;
};

struct soc_zcv_array soc_zcv1[] = {
#include "soc_zcv.h"
};

struct vbat_Q_array vbat_q1[] = {
#include "vbat_q.h"
};

#define RELEASE_CURRENT (2.0)
#define MAX_Q (2670)
#define ARRAY_SZIE(x) (sizeof(x)/sizeof(x[0]))

void main(void)
{
    int i;
    for (i=0; i < ARRAY_SZIE(vbat_q1); i++) {
        vbat_q1[i].q = 100*vbat_q1[i].q/MAX_Q; 
        vbat_q1[i].vbat = vbat_q1[i].vbat*1000; 
    }
    for (i=0; i < ARRAY_SZIE(vbat_q1); i++)
        ;//printf("%8f: %8f\n", vbat_q1[i].vbat, vbat_q1[i].q);

    for (i=0; i < ARRAY_SZIE(soc_zcv1); i++)
        printf("%d: %d\n", soc_zcv1[i].zcv, soc_zcv1[i].soc);
    
    //start to gen soc-zcv
    struct soc_zcv_array *gen_soc_zcv = malloc(ARRAY_SZIE(soc_zcv1)*sizeof(struct soc_zcv_array));
    int second_idx = 0;
    for (i=0; i < ARRAY_SZIE(soc_zcv1); i++) {
        int idx=0;
        for (idx=second_idx; idx < ARRAY_SZIE(vbat_q1); idx++) {
            if (vbat_q1[idx].q == soc_zcv1[i].soc) {
                gen_soc_zcv[i].soc = soc_zcv1[i].soc;
                gen_soc_zcv[i].zcv = vbat_q1[idx].vbat;
                break;
            }
            if (vbat_q1[idx].q > soc_zcv1[i].soc) {
                float delt_soc = vbat_q1[idx].q - vbat_q1[idx - 1].q;
                float delt_vol = vbat_q1[idx].vbat - vbat_q1[idx -1].vbat;
                float t_delt = soc_zcv1[i].soc - vbat_q1[idx -1].q;
                float o_delt = t_delt*delt_vol/delt_soc;
                //printf("\t\tidx: %d=== t_soc_delt:%f ==> t_vol_delt: %f, vol_delt: %f\n", idx, t_delt, o_delt, delt_vol);
                gen_soc_zcv[i].soc = soc_zcv1[i].soc;
                gen_soc_zcv[i].zcv = (vbat_q1[idx-1].vbat + o_delt);

                break;
            }      
        }
        second_idx = idx;
        printf("%d: %d\n", gen_soc_zcv[i].zcv, gen_soc_zcv[i].soc);
    }
    //start to gen rbat-zcv
    struct rbat_zcv_array *out_r_zcv = malloc(ARRAY_SZIE(soc_zcv1)*sizeof(struct rbat_zcv_array));
    for (i=0; i < ARRAY_SZIE(soc_zcv1); i++) {
        out_r_zcv[i].zcv = soc_zcv1[i].zcv;
        out_r_zcv[i].rbat = (soc_zcv1[i].zcv - gen_soc_zcv[i].zcv)/RELEASE_CURRENT;
        if (out_r_zcv[i].rbat < 0)
            out_r_zcv[i].rbat = -out_r_zcv[i].rbat;
        printf("\t{%d, %d},\n", out_r_zcv[i].rbat, out_r_zcv[i].zcv);

    }

}
