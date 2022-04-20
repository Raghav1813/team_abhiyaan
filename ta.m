function result = doWhat(dirPath, isCaseSensitive, ~, ~)
    if isCaseSensitive
        result = what('-casesensitive', dirPath);
    else
        result = what('-caseinsensitive', dirPath);
    end
end

%   Copyright 2007-2021 The MathWorks, Inc.
