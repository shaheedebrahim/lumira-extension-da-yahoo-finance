#SAP Lumira Data Access Extention For Yahoo Finance

By [Shaheed Ebrahim](https://www.shaheedebrahim.com)

A Lumira Data Extension To Fetch Yahoo Stock Information

To use this extension follow these steps:

1. Clone or fork the repository to your computer
2. Download a packaging program like PyInstaller to create an exe out of the YahooExtractor.py code
3. Run the following command `PyInstaller --onefile --windowed YahooExtractor.py` in the directory with the src file
4. Follow step 4 from the following url [http://scn.sap.com/community/lumira/blog/2014/09/12/creating-my-first-data-access-extension-for-lumira]
5. Add the .exe to the new folder that was created in the previous step ("C:\Program Files\SAP Lumira\Desktop\daextensions")
6. Open Lumira, create a new dataset, select external datasource and click next
7. You will now see a file with the same name as the exe you created double click on that
8. Now enter the stock ticker symbol and the start and end dates for the data you will pull.
9. You have now downloaded the information and it is ready to be used!
