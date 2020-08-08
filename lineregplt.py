{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def lineregplt(data,name,factor=1,inperc=0,unit=''):    \n",
    "    ax = sn.lineplot(data.Datetime,data[name])\n",
    "    \n",
    "    # calculate linear trend with poly1d and plot it\n",
    "    lreg = np.poly1d(np.polyfit(np.arange(len(data.Month)), data[name], 1))\n",
    "    plt.plot(data.Datetime, lreg(np.arange(len(data.Month))),color='m');\n",
    "    \n",
    "    # print Trend in sqkm per decade (=>*12*10*1000000) into figure\n",
    "    if inperc == 1:\n",
    "        txt = 'Trend per decade: ' + str((lreg.c[0]*factor).round(1)) +' ',unit+' ('+ \\\n",
    "              str((lreg.c[0]*12*10/SIE_Mon[i].mean()*100).round(2)) +'%)'\n",
    "    else:\n",
    "        txt = 'Trend per decade: ' + str((lreg.c[0]*factor).round(1)) + ' ', unit\n",
    "    plt.text(SIE_Mon.Datetime.iloc[-125],2.4,txt,fontsize=12)\n",
    "    \n",
    "    plt.xlabel('')\n",
    "    plt.xticks(fontsize= 12)\n",
    "    plt.yticks(fontsize= 12)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:nf] *",
   "language": "python",
   "name": "conda-env-nf-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
