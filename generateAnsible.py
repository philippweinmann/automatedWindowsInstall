import getInstalledChocolateyPackages

def addInstallToAnsible(ansibleFile, packageName):
    ansibleFile.write("- name: Install " + packageName + "\n  win_chocolatey:\n    name: " + packageName + "\n    state: present\n\n")

# function generates an ansible playbook (.yml file) in the same directory as this python file.
def generateAnsibleCode():
    packageNameList = getInstalledChocolateyPackages.extractPackageNames()
    ansibleFile = open("generatedAnsibleCode.yml", "w")

    counter = 0
    while counter < len(packageNameList):
        addInstallToAnsible(ansibleFile, packageNameList[counter])
        counter += 1

