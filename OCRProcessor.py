from shutil import copy2

import comtypes.client as cc

import sys


## Folder with FRE dll
# def GetDllFolder():
#     if (is64BitConfiguration()):
#         return "C:\\Program Files\\Distributives\\ABBYY SDK\\11\\FineReader Engine\\Bin64"
#     else:
#         return "C:\\Program Files\\Distributives\\ABBYY SDK\\11\\FineReader Engine\\Bin"


## Return developer serial number for FRE
def GetDeveloperSN():
    return "SWTT-1101-0005-7881-9554-9337"


## Return full path to Samples directory
def GetSamplesFolder():
    return "C:\\ProgramData\\ABBYY\\SDK\\11\\FineReader Engine\\Samples"


## Determines whether the current configuration is a 64-bit configuration
def is64BitConfiguration():
    return sys.maxsize > 2 ** 32


class ABBYYProcessor():
    def __init__(self):
        EngineLoader = cc.CreateObject("FREngine.OutprocLoader")
        Engine = EngineLoader.GetEngineObject("SWTT-1101-0005-7881-9554-9337")


def Run():
    ## Load ABBYY FineReader Engine
    print sys.maxsize
    LoadEngine()
    try:
        ## Process with ABBYY FineReader Engine
        ProcessWithEngine()
    finally:
        ## Unload ABBYY FineReader Engine
        UnloadEngine()


def LoadEngine():
    global Engine
    global EngineLoader

    DisplayMessage("Initializing Engine...")
    EngineLoader = cc.CreateObject("FREngine.OutprocLoader")
    Engine = EngineLoader.GetEngineObject(GetDeveloperSN())


def ProcessWithEngine():
    try:
        ## Setup FREngine
        SetupFREngine()
        ## Process sample image
        ProcessImage()
    except Exception as e:
        DisplayMessage(e)


def SetupFREngine():
    global Engine

    DisplayMessage("Loading predefined profile...")
    Engine.LoadPredefinedProfile("TextExtraction_Accuracy")
    ## Possible profile names are:
    ## "DocumentConversion_Accuracy", "DocumentConversion_Speed",
    ## "DocumentArchiving_Accuracy", "DocumentArchiving_Speed",
    ## "BookArchiving_Accuracy", "BookArchiving_Speed",
    ## "TextExtraction_Accuracy", "TextExtraction_Speed",
    ## "FieldLevelRecognition",
    ## "BarcodeRecognition_Accuracy", "BarcodeRecognition_Speed",
    ## "HighCompressedImageOnlyPdf",
    ## "BusinessCardsProcessing",
    ## "EngineeringDrawingsProcessing",
    ## "Version9Compatibility",
    ## "Default"


def ProcessImage():
    global Engine

    imagePath = GetSamplesFolder() + "\\SampleImages\\Demo.tif"

    ## Don't recognize PDF file with a textual content, just copy it
    if (Engine.IsPdfWithTextualContent(imagePath, None)):
        DisplayMessage("Copy results...")
        resultPath = GetSamplesFolder() + "\\SampleImages\\Demo_copy.pdf"
        copy2(imagePath, resultPath)
        return

    ## Create document
    document = Engine.CreateFRDocument()

    try:
        ## Add image file to document
        DisplayMessage("Loading image...")
        document.AddImageFile(imagePath, None, None)

        ## Process document
        DisplayMessage("Process...")
        document.Process(None)

        ## Save results
        DisplayMessage("Saving results...")
        FEF_RTF = 0
        FEF_PDF = 4
        FEF_TXT = 5
        PES_Balanced = 1

        ## Save results to rtf with default parameters
        rtfExportPath = GetSamplesFolder() + "\\SampleImages\\Demo_Python.rtf"

        document.Export(rtfExportPath, FEF_RTF, None)

        ## Save results to pdf using 'balanced' scenario
        pdfParams = Engine.CreatePDFExportParams()
        pdfParams.Scenario = PES_Balanced

        pdfExportPath = GetSamplesFolder() + "\\SampleImages\\Demo_Python.pdf"
        document.Export(pdfExportPath, FEF_PDF, pdfParams)
    except Exception as e:
        DisplayMessage(e)
    finally:
        ## Close document
        document.Close()


def UnloadEngine():
    global Engine
    global EngineLoader
    DisplayMessage("Deinitializing Engine...")
    Engine = None
    EngineLoader.ExplicitlyUnload()
    EngineLoader = None


def DisplayMessage(message):
    print(message)


try:
    EngineLoader = None
    Engine = None

    Run()
except Exception as e:
    DisplayMessage(e)
