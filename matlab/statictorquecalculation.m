%% Static Torque Calculation Tool (T = m * g * R)
% Author: Gil Soco
% Description:
%   Computes static torque for various masses and lever lengths using:
%               T = m * g * R
%   Includes:
%       - Automatic table generation
%       - Engineering plots
%
%   Outputs:
%       static_torque_results.csv
%       static_torque_plot.png

g = 9.81; % Acceleration due to Gravity (m/s^2)
masses = [3, 7, 10]; % Masses (m) in kg
lever_lengths = 0.1:0.1:1.0; % Lever Lengths (R) in meters (0.1 to 1.0)


num_rows = length(masses) * length(lever_lengths);
Mass = zeros(num_rows, 1);
LeverLength = zeros(num_rows, 1);
StaticTorque = zeros(num_rows, 1);
idx = 1;


scriptFolder = fileparts(mfilename('fullpath'));
projectFolder = fileparts(scriptFolder);
outputFolder = fullfile(projectFolder, 'Images');
if ~exist(outputFolder, 'dir')
    mkdir(outputFolder);
end

% Calculate Torque for every combination
disp('Calculating Static Torque (T = m * g * R)...');
disp('------------------------------------------');

for m = masses
    for R = lever_lengths
        % Static Torque formula
        T = m * g * R;
        
        % Store results
        Mass(idx) = m;
        LeverLength(idx) = R;
        StaticTorque(idx) = T;
        
        idx = idx + 1;
    end
end


TorqueTable = table(Mass, LeverLength, StaticTorque);

TorqueTable.Properties.VariableNames = {'Mass_kg', 'LeverLength_m', 'StaticTorque_Nm'};

disp(' ');
disp('Calculated Static Torque Results');
disp(TorqueTable);


writetable(TorqueTable, 'm-static_torque_results.csv');
disp(' ');
disp('Results also saved to m-static_torque_results.csv');

%% Plot: Torque vs Lever Length for Each Mass
figure;
hold on; grid on;

unique_masses = unique(Mass);

for m = unique_masses'
    idx = (Mass == m);
    plot(LeverLength(idx), StaticTorque(idx), '-o', 'LineWidth', 1.5, ...
        'DisplayName', sprintf('Mass = %d kg', m));
end

xlabel('Lever Length (m)');
ylabel('Static Torque (N·m)');
title('Torque vs Lever Length for Different Masses');
legend('Location', 'northwest');
hold off;

%% Saves the plot as an image .png file
outputName_png = fullfile(outputFolder, 'm-static_torque_plot.png');

exportgraphics(gcf, outputName_png, 'Resolution', 300);   % High-quality PNG

disp(['Plot saved to folder: ' outputFolder]);
