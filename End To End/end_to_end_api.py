# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:01:48 2018

@author: Steven.Broad
"""

# Python .NET interface
from dotnet.seamless import add_assemblies, load_assembly#, build_assembly

# load PLEXOS assemblies
plexos_path = 'C:/Program Files (x86)/Energy Exemplar/PLEXOS 7.5/'
add_assemblies(plexos_path)
load_assembly('PLEXOS7_NET.Core')
load_assembly('EEUTILITY')

from PLEXOS7_NET.Core import DatabaseCore
from EEUTILITY.Enums import *

class PlexosInputDatabase:
    
    db = DatabaseCore()
    def Connection(strfile):
            self.db.Connection(strfile)
    
    
    def GetModelsToExecute(strinputfilename,\
                            strmodellist,\
                            strprojectlist):
            return self.db.GetModelsToExecute(strinputfilename,strmodellist,strprojectlist)
    
    
    def Close():
            self.db.Close()
    
    
    def NewEmptyDatabase(filepath,\
                            overwrite = False):
            return self.db.NewEmptyDatabase(filepath,overwrite)
    
    
    def get_InstallPath():
            return self.db.get_InstallPath()
    
    
    def GetData(tablename,\
                            strfields):
            return self.db.GetData(tablename,strfields)
    
    
    def ObjectId2Name(objectid):
            return self.db.ObjectId2Name(objectid)
    
    
    def ObjectName2Id(classid,\
                            name):
            return self.db.ObjectName2Id(classid,name)
    
    
    def GetObjects(nclassid):
            return self.db.GetObjects(nclassid)
    
    
    def GetInputDataSet():
            return self.db.GetInputDataSet()
    
    
    def AddObject(strname,\
                            nclassid,\
                            baddsystemmembership,\
                            strcategory = None,\
                            strdescription = None):
            return self.db.AddObject(strname,nclassid,baddsystemmembership,strcategory,strdescription)
    
    
    def RemoveObject(strname,\
                            nclassid):
            return self.db.RemoveObject(strname,nclassid)
    
    
    def RenameObject(stroldname,\
                            strnewname,\
                            nclassid):
            return self.db.RenameObject(stroldname,strnewname,nclassid)
    
    
    def UpdateObjectDescription(nclassid,\
                            strobjectname,\
                            strnewdescription):
            return self.db.UpdateObjectDescription(nclassid,strobjectname,strnewdescription)
    
    
    def GetObjectsInCategory(nclassid,\
                            strcategory):
            return self.db.GetObjectsInCategory(nclassid,strcategory)
    
    
    def AddCategory(nclassid,\
                            strcategory):
            return self.db.AddCategory(nclassid,strcategory)
    
    
    def RemoveCategory(nclassid,\
                            strcategory,\
                            bremoveobjects = True):
            return self.db.RemoveCategory(nclassid,strcategory,bremoveobjects)
    
    
    def GetCategories(nclassid):
            return self.db.GetCategories(nclassid)
    
    
    def CategoryExists(nclassid,\
                            strcategory):
            return self.db.CategoryExists(nclassid,strcategory)
    
    
    def CategorizeObject(nclassid,\
                            strobject,\
                            strcategory):
            return self.db.CategorizeObject(nclassid,strobject,strcategory)
    
    
    def CopyObject(strname,\
                            strnewname,\
                            nclassid):
            return self.db.CopyObject(strname,strnewname,nclassid)
    
    
    def GetMemberships(ncollectionid):
            return self.db.GetMemberships(ncollectionid)
    
    
    def AddMembership(ncollectionid,\
                            strparent,\
                            strchild):
            return self.db.AddMembership(ncollectionid,strparent,strchild)
    
    
    def RemoveMembership(ncollectionid,\
                            strparent,\
                            strchild):
            return self.db.RemoveMembership(ncollectionid,strparent,strchild)
    
    
    def GetMembershipID(ncollectionid,\
                            strparent,\
                            strchild):
            return self.db.GetMembershipID(ncollectionid,strparent,strchild)
    
    
    def GetChildMembers(ncollectionid,\
                            strparent):
            return self.db.GetChildMembers(ncollectionid,strparent)
    
    
    def GetParentMembers(ncollectionid,\
                            strchild):
            return self.db.GetParentMembers(ncollectionid,strchild)
    
    
    def AddAttribute(nclassid,\
                            strobjectname,\
                            nattributeenum,\
                            dvalue):
            return self.db.AddAttribute(nclassid,strobjectname,nattributeenum,dvalue)
    
    
    def RemoveAttribute(nclassid,\
                            strobjectname,\
                            nattributeenum):
            return self.db.RemoveAttribute(nclassid,strobjectname,nattributeenum)
    
    
    def UpdateAttribute(nclassid,\
                            strobjectname,\
                            nattributeenum,\
                            dnewvalue):
            return self.db.UpdateAttribute(nclassid,strobjectname,nattributeenum,dnewvalue)
    
    
    def SetAttributeValue(nclassid,\
                            strobjectname,\
                            nattributeenum,\
                            dvalue):
            return self.db.SetAttributeValue(nclassid,strobjectname,nattributeenum,dvalue)
    
    
    def GetAttributeValue(nclassid,\
                            strobjectname,\
                            nattributeenum,\
                            dvalue):
            return self.db.GetAttributeValue(nclassid,strobjectname,nattributeenum,dvalue)
    
    
    def AddProperty(membershipid,\
                            enumid,\
                            bandid,\
                            value,\
                            datefrom,\
                            dateto,\
                            variable,\
                            datafile,\
                            pattern,\
                            scenario,\
                            action,\
                            periodtypeid):
            return self.db.AddProperty(membershipid,enumid,bandid,value,datefrom,dateto,variable,datafile,pattern,scenario,action,periodtypeid)
    
    
    def RemoveProperty(membershipid,\
                            enumid,\
                            bandid,\
                            datefrom,\
                            dateto,\
                            variable,\
                            datafile,\
                            pattern,\
                            scenario,\
                            action,\
                            periodtypeid):
            return self.db.RemoveProperty(membershipid,enumid,bandid,datefrom,dateto,variable,datafile,pattern,scenario,action,periodtypeid)
    
    
    def GetPropertyValue(membershipid,\
                            enumid,\
                            bandid,\
                            value,\
                            datefrom,\
                            dateto,\
                            variable,\
                            datafile,\
                            pattern,\
                            scenario,\
                            action,\
                            periodtypeid):
            return self.db.GetPropertyValue(membershipid,enumid,bandid,value,datefrom,dateto,variable,datafile,pattern,scenario,action,periodtypeid)
    
    
    def PropertyName2EnumId(strparentclassname,\
                            strchildclassname,\
                            strcollectionname,\
                            strpropertyname):
            return self.db.PropertyName2EnumId(strparentclassname,strchildclassname,strcollectionname,strpropertyname)
    
    
    def AddReportProperty(strreportname,\
                            nreportpropertyid,\
                            nphaseid,\
                            reportperiod,\
                            reportsummary,\
                            reportstatistics,\
                            reportsamples):
            self.db.AddReportProperty(strreportname,nreportpropertyid,nphaseid,reportperiod,reportsummary,reportstatistics,reportsamples)
    
    
    def ReportPropertyName2EnumId(strparentclassname,\
                            strchildclassname,\
                            strcollectionname,\
                            strpropertyname):
            return self.db.ReportPropertyName2EnumId(strparentclassname,strchildclassname,strcollectionname,strpropertyname)
    
    
    def ReportPropertyName2PropertyId(strparentclassname,\
                            strchildclassname,\
                            strcollectionname,\
                            strpropertyname):
            return self.db.ReportPropertyName2PropertyId(strparentclassname,strchildclassname,strcollectionname,strpropertyname)
    
    
    def GetEnabledProperties():
            return self.db.GetEnabledProperties()
    
    
    def GetPropertiesTable(collectionid,\
                            parentnamelist = None,\
                            childnamelist = None,\
                            timeslicelist = None,\
                            scenariolist = None,\
                            categorylist = None):
            return self.db.GetPropertiesTable(collectionid,parentnamelist,childnamelist,timeslicelist,scenariolist,categorylist)
    
    
    def AddAssembly(strfilepath,\
                            strnamespace):
            return self.db.AddAssembly(strfilepath,strnamespace)
    
    
    def RemoveAssembly(strfilepath,\
                            strnamespace):
            return self.db.RemoveAssembly(strfilepath,strnamespace)
    
    
    def GetAssemblies():
            return self.db.GetAssemblies()
    
    
    def SetAssemblyEnabled(strfilepath,\
                            strnamespace,\
                            benabled):
            return self.db.SetAssemblyEnabled(strfilepath,strnamespace,benabled)
    
    
    def get_DisplayAlerts():
            return self.db.get_DisplayAlerts()
    
    
    def set_DisplayAlerts(autopropertyvalue):
            self.db.set_DisplayAlerts(autopropertyvalue)
    
    
    def ToString():
            return self.db.ToString()
    
    
    def Equals(obj):
            return self.db.Equals(obj)
    
    
    def GetHashCode():
            return self.db.GetHashCode()
    
    
    def GetType():
            return self.db.GetType()

    def __init__(self, filename):
        self.db = DatabaseCore()
        self.db.Connection(filename)
        
