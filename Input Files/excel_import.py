import os, sys, clr
from shutil import copyfile

# load PLEXOS assemblies
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 8.3/')
clr.AddReference('PLEXOS.ImportExport')
clr.AddReference('EEDataSets')
clr.AddReference('PLEXOS7_NET.Core')

from PLEXOS.ImportExport import MasterRepository, SupportedFormat, ConsoleLogger
from PLEXOS.ImportExport.Import import ImporterType, Importer, ImportOptions
from PLEXOS.ImportExport.Export import Exporter, ExportOptions
from EEDataSets import MasterDataSet
from PLEXOS7_NET.Core import DatabaseCore

def excel_export(database_file, export_file):
    #initialise the repositories
    databaseRepo = MasterRepository()
    exportDataSet = MasterDataSet()
    if os.path.exists(database_file):
        exportDataSet.ReadXml(database_file)
    else:
        DatabaseCore().NewEmptyDatabase(database_file, True)
    databaseRepo.Initialize(exportDataSet)

    if export_file[-5:] == '.xlsx':
        format = SupportedFormat.GetSupportedFormat(ImporterType.Excel)
    else:
        format = SupportedFormat.GetSupportedFormat(ImporterType.Xml)

    #Initialise the logger
    logger = ConsoleLogger()
    exporter = Exporter(databaseRepo)
    options = ExportOptions()
    options.Filepath = export_file
    options.Format = format
    options.ExportObject = None
    options.ExportSettings = True
    success = exporter.PerformExport(logger, options)

    print('<Success>' if success else 'Failed','<Ended>',sep='\n')

def excel_import(database_file, import_file):
    pass

    # initialise the repositories and try to read the XML file
    databaseRepo = MasterRepository()
    inputDataSet = MasterDataSet()
    DatabaseCore().NewEmptyDatabase(database_file, True)
    databaseRepo.Initialize(inputDataSet)

    # Initialise the logger
    logger = ConsoleLogger()

    # Initialise the importer
    # this may throw ArgumentNullException if the master data is invalid
    importer = Importer(databaseRepo, logger)
    importOptions = ImportOptions.Default

    # Try to Validate and import, if false then look at validation errors
    # This may throw exceptions that need to be handles in a try catch statement
    importer.ValidateAndImportAsync(import_file, importOptions)



    # If the import is successful, replace the old XML and write success to console
    # type in q<enter> at the command line to exit
    # if success:
    #     inputDataSet.WriteXml(database_file.Replace(".xml", "_imported.xml"));
    #     print("<Success>")
    #     return
    # else:
    #     # //If the import fails, iterate through the errors in the dataset and write to screen

    #     VRes = importer.ValidateAsync([import_file], importOptions).Result
    #     foreach (DataTable tab in importer.FailedRows.Tables)
    #     {
    #         if (tab.Rows.Count > 0)
    #         {
    #             string Header = string.Empty;
    #             foreach (DataColumn DC in tab.Columns)
    #             {
    #                 Header += $"{DC.ColumnName},";
    #             }
    #             Header.Remove(Header.Length - 1);
    #             Console.WriteLine(Header);
    #             foreach (DataRow DR in tab.Rows)
    #             {
    #                 string LineItem = string.Empty;
    #                 foreach (Object LI in DR.ItemArray)
    #                 {
    #                     LineItem += $"{LI.ToString()},";
    #                 }
    #                 LineItem.Remove(LineItem.Length - 1);
    #                 Console.WriteLine(LineItem);
    #             }
    #         }

    #     }
    #    print("<Failed>")
    x = input('press any key upon completion')

    print("<Ended>")

def main(args):
    # Demo Export
    # output_path is relative to My Documents folder if base folder is not specified
    source_db = r"Input Files/rts_PLEXOS (8.300 R07).xml"
    output_path = r"GitHub/Python-PLEXOS-API/Input Files/Exported.xlsx"
    if os.path.exists(output_path): os.remove(output_path)
    excel_export(source_db, output_path)

    # Demo Import
    import_path = output_path
    import_db = source_db.replace('.xml', '_imported.xml')
    if os.path.exists(import_db): os.remove(import_db)
    excel_import(import_db, import_path)

if __name__ == '__main__':
    main([])
